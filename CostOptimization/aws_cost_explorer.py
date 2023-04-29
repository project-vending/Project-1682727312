
import boto3

# Set up a client for the Cost Explorer service
ce = boto3.client('ce')

# Define the start and end dates for the cost and usage report
start_date = '2022-01-01'
end_date = '2022-01-31'

# Define the query for getting the cost and usage data
query = {
  "TimePeriod": {
    "Start": start_date,
    "End": end_date
  },
  "Granularity": "DAILY",
  "Metrics": [
    "AmortizedCost",
  ],
  "GroupBy": [
    {
      "Type": "DIMENSION",
      "Key": "SERVICE"
    },
  ]
}

# Get the results of the query
response = ce.get_cost_and_usage(
  TimePeriod=query['TimePeriod'],
  Granularity=query['Granularity'],
  Metrics=query['Metrics'],
  GroupBy=query['GroupBy']
)

# Get the cost by service for each day in the date range
results = response['ResultsByTime']
for result in results:
  print(f"Date: {result['TimePeriod']['Start']}")
  for group in result['Groups']:
    service = group['Keys'][0]
    cost = group['Metrics']['AmortizedCost']['Amount']
    print(f"  Service: {service} Cost: {cost}")
