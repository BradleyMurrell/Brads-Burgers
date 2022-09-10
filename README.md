# ***Brad's Burgers***

<a name="table-of-contents"></a>
## Table of Contents

* [Description](#description)
* [User Stories](#user-stories)
* [Wireframe](#wireframe)
* [Structure](#structure)
    * [App Flow](#app-flow)
    * [Data Schema](#data-schema)
* [Models](#models)
* [Features](#features)
* [Colors Used](#colors-used)
* [Testing](#testing)
* [Validator Testing](#validator-testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Content](#content)

<a name="description"></a>
## Description

For my project, I have created an ordering system for a burger restaurant called ***Brad's Burgers***.

The idea of the ordering system is that when the customer arrives to the restaurant, they will make their order on a terminal.

The customer will first see the home screen which will prompt them to ***Place Order***.

After ***Place Order*** has been selected, the screen will show a list of categories to choose from, ***Burgers***, ***Sides*** and ***Drinks***.

After selecting a category, the customer will have a choice of selecting from a list of the chosen category.

When the customer has finished with their order, they will see a table on the order page what they have ordered and the total cost.

The customer can remove items from the order list.

When they are happy with the order, the customer can select the ***Finish Order*** button which will dirict them to a final page displaying their order number.

The restaurant will then be able to see the orders that have been made along with the order number.

When the order is complete, the restaurant can mark the order as complete.

[Back to top](#table-of-contents)

------

<a name="user-stories"></a>
## User Stories

| ***As a*** | ***I want to be able to*** | ***so that I can*** |
| ------ | ------ | ------|
| customer | select from a number of categories | order a meal |
| customer | view what I have ordered | see the total price before finishing my order |
| customer | select items from my order | remove item from the order list |
| restaurant worker | login to an account | edit product information |
| restaurant worker | view orders that have been made along with the order number | fulfill an order correctly |
| restaurant worker | mark which orders are complete | I don't make the same order twice |

[Back to top](#table-of-contents)

------

<a name="wireframe"></a>
## Wireframe

### ***Homepage***
![homepage](docs/index.html.png)
### ***Order Page***
![orderpage](docs/order.html.png)
### ***Burgers Page***
![burgerspage](docs/burgers.html.png)
### ***Sides Page***
![sidespage](docs/sides.html.png)
### ***Drinks Page***
![drinkspage](docs/drinks.html.png)
### ***Order Confirmation page***
![orderconfirmation](docs/order_confirmation.html.png)

------

<a name="struture"></a>
## Structure

<a name="app-flow"></a>
### App Flow

### ***Customer***
![customer](docs/customer.png)

### ***Admin***
![admin](docs/admin.png)

[Back to top](#table-of-contents)

------

<a name="data-schema"></a>
### Data Schema

### ***Products***
![products](docs/products.png)

### ***Orders***
![orders](docs/orders.png)

[Back to top](#table-of-contents)

------

<a name="models"></a>
## Models

***Products***

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ----|
| name | | CharField | max_length=50 |
| price | | DecimalField | max_digits=6, decimal_places=2 |
| image_url | | URLField | max_length=80 |

***Orders***

| Name | Key | Type | Other Details |
| ---- | ---- | ---- | ----|
| order_number | | CharField | max_length=50 |
| time_date | | DateTimeField | auto_now_add=True |
| order_total | | DecimalField | max_length=10, decimal_places=2, default=0 |

[Back to top](#table-of-contents)

------

<a name="features"></a>
## Features

### Existing Features
* Customer can order their meal by selecting from a number of categories
* Customer can view what they have ordered with the price of each item and a total price before finishing their order
* Customer can remove item from order list
* Customer will be given an order number after finishing their order
* Restaurant can view what orders have been made along side the order number
* Restaurant can mark which orders have been completed

### Future Features
* Customer can make a payment with debit/credit card after completing order
* Customer can register their details and order/pay online
* Customer can have the option for home delivery
* Restaurant can show what items are out of stock
* Customer can customize their burger by selecting what they want on it from a number of sub-categories

[Back to top](#table-of-contents)

------

Site screenshots go here!

[Back to top](#table-of-contents)

------

<a name="colors-used"></a>
## Colors Used

| Color | Hex | Bootstrap name |
| ---- | ---- | ---- |
| ![78c2ad](docs/78c2ad.jpeg) | #78C2AD | Primary |
| ![f3969a](docs/f3969a.jpeg) | #F3969A | Secondary |
| ![56cc9d](docs/56cc9d.jpeg) | #56CC9D | Success |
| ![6cc3d5](docs/6cc3d5.jpeg) | #6CC3D5 | Info |
| ![ffce67](docs/ffce67.jpeg) | #FFCE67 | Warning |
| ![ff7851](docs/ff7851.jpeg) | #FF7851 | Danger |
| ![f8f9fa](docs/f8f9fa.jpeg) | #F8F9FA | Light |

[Back to top](#table-of-contents)

------

<a name="testing"></a>
## Testing

[Back to top](#table-of-contents)

<a name="validator-testing"></a>
## Validator Testing

### HTML

| File Name | File Path | Result | W3C | Comment |
| ----- | ----- | ----- | ----- | -----|
| base.html | templates/base.html | PASS | [link](docs/basetest.png) |
| index.html | home/templates/index.html | PASS | [link](docs/indextest.png) |

[Back to top](#table-of-contents)

------

<a name="bugs"></a>
## Bugs

## Fixed Bugs

| Commit | File Name | Line | Comment |
| ----- | ----- | ----- | -----|
| [aff9f79](https://github.com/BradleyMurrell/brads-burgers/commit/aff9f793f8096d483f3e0a0d99ba946787310745) | settings.py | 65 | changed `'DIRS': [TEMPLATES_DIRS],` to `'DIRS': [TEMPLATES_DIR],` |

[Back to top](#table-of-contents)

------

<a name="deployment"></a>
## Deployment
This project was deployed using Heroku
* Steps for deployment
  * Create a Heroku app
  * Change `DEBUG` in ***settings.py*** to `False`
  * Link the Heroku app to the repository
  * Click on deploy

[Back to top](#table-of-contents)

------
<a name="credits"></a>
## Credits
* Simen Daehlin (mentor) for help and advice
* Code Institute for the deployment instructions

[Back to top](#table-of-contents)

------

<a name="content"></a>
## Content
* Wireframe created on https://whimsical.com/
* Bootstrap CDN sourced from https://bootswatch.com/minty/
