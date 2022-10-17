from django.shortcuts import render

def predict_view(request):
    return render(request, "index.html")


def predict_chances(request):

    # import the necessary packages
    import pandas as pd

    # Receive data from client
    sepal_length = float(request.POST.get('sepal_length'))
    sepal_width = float(request.POST.get('sepal_width'))
    petal_length = float(request.POST.get('petal_length'))
    petal_width = float(request.POST.get('petal_width'))


    # unpickle the model
    try:
        model = pd.read_pickle('model.pkl')
        print('Model loaded')
    except Exception as e:
        print('Model not loaded. Error: ', e)

    from django.http import JsonResponse

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    # Take the first value of prediction
    classificaton = prediction[0]

    # save data into database
    from .models import ModelPredict
    ModelPredict.objects.create(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width,
        prediction=classificaton
    )

    # Send the prediction back to the client
    data = {
        'prediction': classificaton
    }
    
    # Return the prediction as a json object
    return JsonResponse({'result': classificaton, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


def result_view(request):
    from .models import ModelPredict
    data = ModelPredict.objects.all()
    return render(request, "resultDB.html", {'logs': data})