import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SalesData
from django.db.models import Count, Sum, Avg  # Import Count

# Extract Data
def extract_data(file_path):
    return pd.read_csv(file_path)

# Transform Data
def transform_data(df, region):
    # Convert columns to appropriate types
    df['QuantityOrdered'] = pd.to_numeric(df['QuantityOrdered'], errors='coerce')
    df['ItemPrice'] = pd.to_numeric(df['ItemPrice'], errors='coerce')
    df['PromotionDiscount'] = pd.to_numeric(df['PromotionDiscount'], errors='coerce')
    
    # Fill missing numeric values with 0 (optional, based on your data)
    df[['QuantityOrdered', 'ItemPrice', 'PromotionDiscount']] = df[['QuantityOrdered', 'ItemPrice', 'PromotionDiscount']].fillna(0)
    
    # Add calculated columns
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']
    df['region'] = region
    df['net_sales'] = df['total_sales'] - df['PromotionDiscount']
    
    # Drop duplicates and filter out invalid sales
    df = df.drop_duplicates(subset='OrderId')
    df = df[df['net_sales'] > 0]
    return df


# Load Data into Database
def load_data_to_db(df):
    for _, row in df.iterrows():
        SalesData.objects.update_or_create(
            order_id=row['OrderId'],
            defaults={
                'order_item_id': row['OrderItemId'],
                'quantity_ordered': row['QuantityOrdered'],
                'item_price': row['ItemPrice'],
                'promotion_discount': row['PromotionDiscount'],
                'total_sales': row['total_sales'],
                'region': row['region'],
                'net_sales': row['net_sales'],
            },
        )

# Main ETL Process
@csrf_exempt
def etl_process(request):
    try:
        # Extract
        df_a = extract_data('csvFiles/order_region_a.csv')
        df_b = extract_data('csvFiles/order_region_b.csv')
        
        # Debug: Check extracted data
        print(f"Extracted {len(df_a)} records from Region A")
        print(f"Extracted {len(df_b)} records from Region B")
        
        # Transform
        df_a = transform_data(df_a, 'A')
        df_b = transform_data(df_b, 'B')

        # Debug: Check transformed data
        print(f"Transformed Region A: {df_a.head()}")
        print(f"Transformed Region B: {df_b.head()}")
        
        # Combine
        df_combined = pd.concat([df_a, df_b], ignore_index=True)
        
        # Debug: Check combined data
        print(f"Combined Data: {df_combined.head()}")

        # Load
        load_data_to_db(df_combined)

        return JsonResponse({"status": "success", "message": "ETL process completed successfully."})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})


@csrf_exempt
def retrieve_data(request):
    try:
        # Total records
        total_records = SalesData.objects.count()
        
        # Total sales by region
        sales_by_region = SalesData.objects.values('region').annotate(total_sales=Sum('total_sales'))
        
        # Average sales
        avg_sales = SalesData.objects.aggregate(avg_sales=Avg('total_sales'))['avg_sales']
        
        # Duplicate orders
        duplicate_orders = SalesData.objects.values('order_id').annotate(count=Count('order_id')).filter(count__gt=1).count()
        
        # Prepare response
        response = {
            "total_records": total_records,
            "sales_by_region": list(sales_by_region),
            "average_sales": avg_sales,
            "duplicate_orders": duplicate_orders,
        }
        
        return JsonResponse({"status": "success", "data": response})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

