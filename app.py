import speedtest
import socket


def check_connection():
    try:
        socket.create_connection(('www.google.com', 80))
        return True
    except OSError:
        pass
    return False

def speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    print(f"Download Speed: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {upload_speed / 1_000_000:.2f} Mbps")
    
conn = check_connection()

if conn is True:
    print('Checking your speed....\n')
    speed_test()
else:
    print("Check Your Internet Connection!!")
