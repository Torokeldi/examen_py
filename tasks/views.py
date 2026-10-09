from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()

        completed = self.request.query_params.get("completed")

        if completed is not None:
            if completed.lower() == "true":
                queryset = queryset.filter(completed=True)
            elif completed.lower() == "false":
                queryset = queryset.filter(completed=False)

        return queryset
