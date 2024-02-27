import time
from abc import ABC, abstractmethod

class Scheduler(ABC):
    @abstractmethod
    def schedule_task(self, task):
        pass

class TenSecondScheduler(Scheduler):
    def schedule_task(self, task):
        import os

        while True:
            task()
            time.sleep(os.getenv("SLEEP_TIME", 10))

class ContainerInfoTask:
    """
    A task that fetches and prints container information.
    """

    def __call__(self):
        from utils.docker_fetcher import ContainerInfoFetcherFactory

        fetcher = ContainerInfoFetcherFactory.create_fetcher()
        container_info = fetcher.fetch_info()
        print(container_info)

# def main():
#     scheduler = TenSecondScheduler()
#     task = ContainerInfoTask()
#     scheduler.schedule_task(task)

# if __name__ == "__main__":
#     main()