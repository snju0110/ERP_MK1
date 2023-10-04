from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *


def login(request):
    if request.method == 'POST':
        name = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)
        print(name, "    ", password)
        if user is not None:
            auth.login(request, user)
            print("Logged in as ", user)
            return redirect('landingpage')  # Landing page
        else:
            print("login failed")
            # messages.info(request, "Check User name or password")
            # return render(request, "login_page.html")
            return render(request, 'login.html')
    else:
        pass
    return render(request, 'login.html')


def check_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password, "------------------------------------")

    return render(request, 'login.html')


def landingpage(request):
    return render(request, 'dashboard.html')


def login_page(request):
    if request.method == 'POST':
        name = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)
        print(name, "    ", password)
        if user is not None:
            auth.login(request, user)
            print("Logged in as ", user)
            context = {
                'user': user,
            }
            return redirect('landingpage')  # Landing page
        else:
            print("login failed")
            # messages.info(request, "Check User name or password")
            # return render(request, "login_page.html")
            return render(request, 'login.html')
    else:
        pass
    return render(request, 'login.html')


def stockupdate(request):
    uom = settings_uom.objects.values_list('uom', flat=True)
    supplier_list = settings_supplier_list.objects.values_list('supplier', flat=True)
    payment_status = settings_payment_status.objects.values_list('payment_status', flat=True)
    purchase_status = settings_purchase_status.objects.values_list('purchase_status', flat=True)
    godowns = settings_godown_list.objects.values_list('godown_list', flat=True)
    product = settings_product.objects.all()
    context = {

        'godowns': godowns,
        'payment_status': payment_status,
        'purchase_status': purchase_status,
        'supplier_list': supplier_list,
        'uom': uom,
        'product': product

    }

    return render(request, 'stock_update.html', context)


def input_data(request):
    return render(request, 'forms-input-groups.html')


def stock_update_save(request):
    if request.method == 'POST':
        godown = request.POST['godown']
        supplier = request.POST['supplier']
        purchase_status = request.POST['purchase_status']
        brand = request.POST['brand']
        variant = request.POST['variant']
        sub_variant = request.POST['sub_variant']
        payment_status = request.POST['payment_status']
        hsn_code = request.POST['hsn_code']
        invoice_number = request.POST['invoice_number']
        quantity = request.POST['quantity']
        uom = request.POST['uom']
        price = request.POST['price']
        due = request.POST['due']
        cgst = request.POST['cgst']
        sgst = request.POST['sgst']
        igst = request.POST['igst']

        print(godown, supplier, purchase_status, payment_status, hsn_code, invoice_number, quantity, uom, price, due,
              cgst, sgst, igst)

        data = stock_update(godown=godown,
                            supplier_name=supplier,
                            purchase_status=purchase_status,
                            payment_status=payment_status,
                            variant=variant,
                            brand=brand,
                            sub_variant=sub_variant,
                            hsn_code=hsn_code,
                            invoice_num=invoice_number,
                            quantity=quantity,
                            uom=uom,
                            price=price,
                            due=due,
                            cgst=cgst,
                            igst=igst,
                            sgst=sgst,
                            date='2023-09-01',
                            )
        data.save()

    return render(request, 'dashboard.html')


def stock_update_table(request):
    query1 = stock_update.objects.all()
    context = {
        'table_data': query1
    }

    return render(request, 'Stock_update_table.html', context)


def update_stock(request):
    uom = settings_uom.objects.values_list('uom', flat=True)
    supplier_list = settings_supplier_list.objects.values_list('supplier', flat=True)
    payment_status = settings_payment_status.objects.values_list('payment_status', flat=True)
    purchase_status = settings_purchase_status.objects.values_list('purchase_status', flat=True)
    godowns = settings_godown_list.objects.values_list('godown_list', flat=True)
    product = settings_product.objects.all()
    context = {

        'godowns': godowns,
        'payment_status': payment_status,
        'purchase_status': purchase_status,
        'supplier_list': supplier_list,
        'uom': uom,
        'product': product

    }
    return render(request, 'POC_Form.html', context)


def save_stock_data(request):
    if request.method == 'POST':
        count = int(request.POST['count'])
        for i in range(1, count + 1):
            globals()['sub_variant' + str(i)] = request.POST['sub_variant' + str(i)]
            globals()['variant' + str(i)] = request.POST['variant' + str(i)]
            globals()['uom' + str(i)] = request.POST['uom' + str(i)]
            globals()['qty' + str(i)] = request.POST['qty' + str(i)]
            globals()['hsn_name' + str(i)] = request.POST['hsn_name' + str(i)]
            globals()['price' + str(i)] = request.POST['price' + str(i)]

        godown = request.POST['godown']
        supplier = request.POST['supplier']
        purchase_status = request.POST['purchase_status']
        # brand = request.POST['brand']
        payment_status = request.POST['payment_status']
        invoice_number = request.POST['invoice_Number']
        due = request.POST['Payed']
        cgst = request.POST['cgst']
        sgst = request.POST['sgst']
        igst = request.POST['igst']

        for i in range(1, count + 1):
            data = stock_update(godown=godown,
                                supplier_name=supplier,
                                purchase_status=purchase_status,
                                payment_status=payment_status,
                                variant=globals()['variant' + str(i)],
                                brand='brand',
                                sub_variant=globals()['sub_variant' + str(i)],
                                hsn_code=globals()['hsn_name' + str(i)],
                                invoice_num=invoice_number,
                                quantity=globals()['qty' + str(i)],
                                uom=globals()['uom' + str(i)],
                                price=globals()['price' + str(i)],
                                due=due,
                                cgst=cgst,
                                igst=igst,
                                sgst=sgst,
                                date='2023-09-01',
                                )
            data.save()



    # return JsonResponse({'value': [count]}, safe=False)
    return render(request , 'dashboard.html')


def update_outward(request):
    context = {

        's':'s'

    }

    return render(request, 'outwards_form.html', context)


def view_stock_detail(request):
    query1 = stock_update.objects.all()
    context = {
        'table_data': query1
    }

    return render(request, 'view_stock_detail.html' , context)

def view_outwards_detail(request):

    return render(request, 'dashboard.html' )
