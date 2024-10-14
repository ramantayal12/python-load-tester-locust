from locust import HttpUser, task, between

class EventPublisherLoadTest(HttpUser):

    @task
    def post_event_payload(self):
        payload = {
            "eventName": "UPI_Pay_Result_Test_Event",
            "timestamp": 1728894536808,
            "payload": "string",
            "source": "upi_payments",
            "merchantIds": ["EVENT_PUBLISHER"],
            "eventRefId": "ref_1"
        }

        self.client.post(
            "/growwpay/events/post-event-payload",
            json=payload,
            headers={
                'Accept': '*/*',
                'Content-Type': 'application/json'
            }
        )

        # Check if the response status is 200 OK
        if response.status_code != 200:
            print(f"Failed Request: {response.status_code}, {response.text}")

    # Set the host of your application
    host = "http://10.150.39.188:9009"
