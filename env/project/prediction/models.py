from django.db import models


# class PredictionModel(models.Model):
#     # Add the fields for the model here
#     sepal_length = models.FloatField()
#     sepal_width = models.FloatField()
#     petal_length = models.FloatField()
#     petal_width = models.FloatField()


# class ResultModel(models.Model):
#     # Add the fields for the model here
#     prediction = models.CharField(max_length=100)
#     probability = models.FloatField()

#     def __str__(self):
#         return self.prediction + " --> " + str(self.probability)


class ModelPredict(models.Model):
    # Add the fields for the model here
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    prediction = models.CharField(max_length=100)
    

    try:
        def __str__(self):
            return self.prediction
    except Exception as e:
        print(e)

        