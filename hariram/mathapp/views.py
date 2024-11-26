from django.shortcuts import render 
def Power(request): 
    context={} 
    context['Power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I= request.POST.get('Intensity','0')
        R= request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        Power= int(I)**2 * int(R) 
        context['Power'] = Power
        context['I'] = I
        context['R'] = R 
        print('Power=',Power) 
    return render(request,'mathapp/math.html',context)


