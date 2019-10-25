# Universal Backend
## What is this?
One thing we do in almost every hackathon is develop a backend that accesses some kind of database, stores and reads stuff and is accessible as a REST-API.
So if you take a step back, we usually need a HTTP-Database-Adaper.

The universal backend takes that idea ad extremum.
It allows you to store any json-encoded data easily and persistently.

## Get Started
Install [docker](https://docs.docker.com/docker-for-mac/install/) first. Then run `docker-compose up`. That's it.

## Usage
You need three HTTP-Request types: `GET`, `POST` and `DELETE`.
Also your requests need to be authenticated with basic authentication according to the username password combination in the docker-compose file.

If you `POST` a certain url, whatever json-encoded data is in your request body is stored in the database.

If you then `GET`that url again, the stored data is returned.

A simple `DELETE` deletes the data.
It's easy like that!

## Advanced Usage
Imagine you have three datapoints at `example.com/api/1`, `example.com/api/2`and `example.com/api/3`, you can access all three of them
as an array when you `GET` `example.com/api`, as long as there is no datapoint associated to `example.com/api`.