from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(Requests):
    if Requests.method == 'POST':
        listing_id = Requests.POST['listing_id']
        listing = Requests.POST['listing']
        name = Requests.POST['name']
        email = Requests.POST['email']
        phone = Requests.POST['phone']
        message = Requests.POST['message']
        user_id = Requests.POST['user_id']
        realtor_email = Requests.POST['realtor_email']

        # If submitted before
        if Requests.user.is_authenticated:
            user_id = Requests.user.id
            has_submitted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_submitted:
                messages.error(Requests, 'You have already submitted requests for this property.')
                return redirect('/listings/'+listing_id)

            else:
                contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone,
                                  message=message, user_id=user_id)
                contact.save()
                # Send Email
                send_mail(
                    'Property Inquiry Requested',
                    'There is a inquiry for ' + listing + '. Login to your admin account for more information. /n From /n BT Real Estate',
                    'minar.rahmnn@gmail.com',
                    ['minar.rhman@gmail.com'],
                    fail_silently= True
                )
                messages.success(Requests, 'Your query has been submitted. We\'ll get back to you soon.')
                return redirect('/listings/' + listing_id)
        else:
            contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone,
                                  message=message, user_id=user_id)
            contact.save()
            send_mail(
                    'Property Inquiry Requested',
                    'There is a inquiry for ' + listing + '. Login to your admin account for more information.'
                                                          'From '
                                                          'BT Real Estate',
                    'minar.rahmnn@gmail.com',
                    ['minar.rhman@gmail.com'],
                    fail_silently=False
                )
            messages.success(Requests, 'Your query has been submitted. We\'ll get back to you soon.')
            return redirect('/listings/' + listing_id)
    else:
        return render(Requests, 'accounts/dashboard.html')
