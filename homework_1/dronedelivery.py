import sys

def main():

    #get the number of routes as n
    n = int(input().strip())

    #get the routes and save to list
    route_input = input().split()
    distances = []

    for i in range(n):
        distances.append(int(route_input[i]))

    


if __name__ == "__main__":
    main()