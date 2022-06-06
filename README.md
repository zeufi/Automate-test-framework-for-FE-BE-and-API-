
![Logo](https://pngtree.com/so/25d)


# Framework for FE, BE, and API

In this project focus on how to do api testing using Postman, it also show how to build an automated test framework combining FE, BE, and API. Finally it reveals how to deploy it in DockerHub and run it in container.
 


## Features

- HTTP Requests Validations
- Data Driven Testing HTML Reports
- Run postman collection/requets from command line
- Framework combining FE, BE, and API
- Deploy and run the Framework on docker


## API Reference

#### Get all items

```http
  GET /api/computers/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Not Required**. Your API key |

#### Get item

```http
  GET /api/computers/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



## Documentation
### API testing with Postman
The CRUD_Validation.xlsx is the test design file with contains requests and tests validations. The DataDrivenTesting.csv contains data needed to perform Data Driven Testing.
The CRUD_Validation.postman_collection.json and QA.postman_environment.json are files necessary to run postman collection/requets from command line.

[Documentation](https://teamjojo.postman.co/workspace/Task2~68c91dcd-d20c-4284-9e4e-c4b3e6ad370c/documentation/7804417-a7d7f29d-759d-4e90-830b-c91a53f95ba6)
### Framework combining FE, BE, and API
The aim of this framework is to automate all test cases which could be done in the frontend and backend side (API and Database) of the application. For example, the creation of a new computer through the API using Postman (with the validation of the response) and a query to the DB to check if new computer has been created will be automate.
Just another framework? Let’s see what will be benefit using this framework:
-	Using our own built framework free
-	Save time 
-	Avoid tasks repetition
-	Avoid human errors 
-	Save memory RAM and graphical memory
-	More productive for QA Engineer
[Documentation](https://behave.readthedocs.io/en/stable/behave.html)
### Deploy and run the Framework on docker
Allow us to ensure the platform independent of our framework and more concept of DevOps.
[Documentation](https://www.docker.com/)



## Installation

Install my-project with docker
```bash
  docker pull mydock987/my_task2
```

Install my-project with git
```bash
  git clone https://github.com/zeufi/Automate-test-framework-for-FE-BE-and-API-.git
```
    
## Usage/Examples

```python
behave -k --no-capture -t tcid01 -D browser=headlesschrome -c -f allure_behave.formatter:Allure
Formatter -o allureReport
allure serve allureReport ->generate the html file
```
```docker
docker run -it taks2 /bin/bash
```



## Appendix

Pre-requisites before running postman collection/requets from command line:
- Inastall Node.js
- Install newman
To generate html report install newman-reporter-html



## Feedback

If you have any feedback, please reach out to us at zeufackjojo@yahoo.fr


## FAQ

#### python modulenotfounderror

python setup.py install
python setup.py develop

#### behave command not found

Run behave under the tests folder


## Authors

- [@zeufi](https://www.github.com/octokatherine)

