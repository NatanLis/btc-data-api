from datetime import datetime

def transform_query_job(query_job):
    """
    Transform BigQuery query results into JSON format.

    Args:
        query_job: QueryJob object containing the results from BigQuery.

    Returns:
        str: JSON string representation of the transformed data.
    """

    transformed_data = [
        {
            "Open_time": row['Open_time'],
            "Open": row['Open'],
            "High": row['High'],
            "Low": row['Low'],
            "Close": row['Close'],
            "Volume": row['Volume'],
            "Close_time": row['Close_time'],
            "Quote_Asset_Volume": row['Quote_Asset_Volume'],
            "Number_of_Trades": row['Number_of_Trades'],
            "Taker_Buy_Base_Asset_Volume": row['Taker_Buy_Base_Asset_Volume'],
            "Taker_Buy_Quote_Asset_Volume": row['Taker_Buy_Quote_Asset_Volume'],
        }
        for row in query_job
    ]

    transformed_data.sort(key=lambda x: x['Open_time'])
    return transformed_data
