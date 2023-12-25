from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def localhost(self):
        self.client.get("https://form.care4all.in/students/80312666")