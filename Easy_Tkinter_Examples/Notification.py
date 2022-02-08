import win10toast

toaster = win10toast.ToastNotifier()

toaster.show_toast('Python', 'Success! This is working!', duration=10)
