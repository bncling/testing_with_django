from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
@login_required
def secret(request):
	if request.user.username == "benclingenpeel":
		return render(request, "users/secret.html")
	else:
		raise PermissionDenied