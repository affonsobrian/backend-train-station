# Backend Train Station

## Deployed version:

To see if the application is running

https://train-departure.herokuapp.com/

To see all possible stations:

https://train-departure.herokuapp.com/stations/

To see departures from a specific station (remember to change the last string in the url for the code of the station that you want to see):

```
https://train-departure.herokuapp.com/departures/<station_code>
```

Example:

https://train-departure.herokuapp.com/departures/BERHBL


## How to run locally?

Run the following command to install the dependencies:

```
pipenv install --dev
```

After installing the dependencies is necessary to configure the local variables, in order to do this run:

```
cp local.env .env
```

Edit the .env file and set the *OCP_API_KEY* var with your api key. 

Finally run the following commands to run the application:

```
pipenv shell
hypercorn controller:app --reload
```

## How to run tests?

Install the dependencies with the following command:
```
pipenv install --dev
```

Run the following command to run the tests:

```
make test
```
