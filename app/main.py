from controller.get_data_from_file import GetData

def main():
    print("hello")

if __name__ == "__main__":
    main()
    data_file = GetData("./files/test-file.csv")
    data_file.get_data_into_dict()