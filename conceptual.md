### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

The important differences that exist between Python and JavaScript is that Python is a general purpose programming language which includes differences in their design, syntax and use cases.  In web development Python is mainly used for back-end development whereas JavaScript can be used for both back-end and front-end development.  Python is executed through a Python interpreter where as JavaScript is typpically executed by web browsers on the front end and Node.js on the backend


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  > Can use the get() method and set a default value.  i.e:  value = rand-dict.get(key, "key not found")

  > The other way this can be done is using the in operator to check if the key exists in the dictionary and if it does not to print out a "key not found statement":
  > if key in my_dict:  
  >    value = my_dict[key]  
  > else:  
  >     value = "key not found"  

  > A third possible way would be to use a try and except:  
  > try:   
  >     value = my_dict["c"]  
  > except KeyError:  
  >     value = "Key not found"  

- What is a unit test?
  > A unit test tests for one small piece of an app at a time - such as a single function.  Essentially it is checking to see "does this individual component work"

- What is an integration test?
  > An integration test, tests multiple units(pieces) and how they interact.  For integration tests, units are combined and tested as groups in multiple ways.  Integration tests can range in complexity.

- What is the role of web application framework, like Flask?
  > Web application frameworks like Flask handles web requests, produce dynamic HTML, handle forms, cookies, connect to databases, provide user log-in/log-out, cache pages for performances etc...It helps define which requests to respond to and how to respond to  
  > requests.  Web Frameworks are limilar to libraries but are bigger and more opionated. Therefore reducing the effort required to develop web applicaitons, while providing a range of tools and features for web development


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  > Parameters in a route would usually be predefined or categorical so foods/pretzel would only work if the input is pretzels and would not route if one attempted to do food/icecream.  Using a URL query param like foods?type would be more suited for search based routing

- How do you collect data from a URL placeholder parameter using Flask?
  
  > It can be specified as a variable in the app.route and then use that variable as a parameter in the routing function  
  > @app.route(/food/<favfoods>)  
  > def my_foods(fav_foods)  
  > return f"My favorite food is {favfoods}"  

- How do you collect data from the query string using Flask?
  
  > we can use the request.args dictionary i.e request.args.get('type')

- How do you collect data from the body of the request using Flask?
  
  > The data can be obtained via a post request in the body using a request.form dictionary i.e request.form.get('type')

- What is a cookie and what kinds of things are they commonly used for?
  
  > Cookies are a way to store small bits of information on the browser(client).  They are name/string-value pairs in which the server tells the client to store.  The client then sends the cookies to the server with each request.  Ultimately it is a way to store information about the user or interaction with a website.  Flask sessions are powered by cookies

- What is the session object in Flask?
  
  > A session object in Flask uses cookies to store unique session ID on the client-side and are a "magic dictionary" of sorts. It allows for the storing of user specific information such as authentication details, preferences, eithout the need to pass the data back and > forth in each request.  The session data is serialized and signed so susers can see but unable to change therir actual session data.

- What does Flask's `jsonify()` do?
  
  > Takes Python objes or data and coversts it into JSON format and also sets the necessary inforamtion in the response so that the client knows that the response contains JSON data.  