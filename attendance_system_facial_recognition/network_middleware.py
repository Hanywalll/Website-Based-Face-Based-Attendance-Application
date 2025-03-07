from django.http import HttpResponse
import os

class NetworkValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Periksa apakah perangkat terhubung ke gateway Telkomsel
        allowed_gateway = '192.168.109.185'  # Default Gateway hotspot Telkomsel Anda
        current_gateway = self.get_default_gateway()

        if current_gateway != allowed_gateway:
            return self.access_denied_page()

        response = self.get_response(request)
        return response

    def get_default_gateway(self):
        try:
            # Ambil informasi gateway aktif dari routing tabel
            with os.popen('route print 0.0.0.0') as route_info:
                lines = route_info.readlines()
                for line in lines:
                    if "0.0.0.0" in line:
                        parts = line.split()
                        return parts[2]  # Gateway IP biasanya berada di kolom ke-3
        except Exception:
            return None

    def access_denied_page(self):
        # HTML yang dirancang lebih menarik
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akses Ditolak</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000; /* Dark background */
            color: #ffc107; /* Text color */
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            padding: 20px;
            background-color: #333; /* Dark background for container */
            border: 1px solid #ffc107; /* Border with the same yellow color */
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5); /* Slight shadow */
        }
        h1 {
            font-size: 2em;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.2em;
        }
        .btn {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #ffc107; /* Yellow background */
            color: #000; /* Dark text for button */
            text-decoration: none;
            border-radius: 5px;
            font-size: 1em;
        }
        .btn:hover {
            background-color: #d4a106; /* Darker yellow on hover */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Akses Ditolak</h1>
        <p>Perangkat Anda tidak terhubung ke WiFi SMPN BandarKedungMulyo.</p>
        <a href="#" class="btn" onclick="location.reload()">Coba Lagi</a>
    </div>
</body>
</html>
"""

        return HttpResponse(html_content, status=403)
