import swagger_client

def main():
    api = swagger_client.ApivApi()
    print api.get_api_resources()
    # print api.list_endpoints()

if __name__ == "__main__":
    main()
