from flask import Flask,render_template,request #Flask needed for web application API, render_template for returning template,request for accessing user input

app = Flask(__name__) #app define or initialization of flask object app with name function


@app.route('/', methods= ['GET','POST']) #As no path defined after / so by default this will get called upon API URL hit, 
                                        #GET is for web application it will accept input from index page,
                                        #Post is for from postman also we can call this
def home_page(): #sample function
    return render_template('index.html')

@app.route('/math', methods = ['POST']) #We need to specify /math in API URL to get this called.
def math_operation(): #sample function to perform math operation.
    if request.method == "POST":
        print('in math operation function')
        operation = request.form['operation']
        print(operation)
        num1 = int(request.form['fnum'])
        print(operation)
        num2 = int(request.form['snum'])

        if operation == 'add':
            print('in add operation')
            r = num1 + num2
            math_result = 'Sum of '+str(num1) + ' and ' +str(num2) +' is ' +str(r)

        if operation == 'substart':
            r = num1 - num2
            math_result = 'Substraction of '+str(num1) + ' and ' +str(num2) +' is ' +str(r)

        if operation == 'multiply':
            r = num1 * num2
            math_result = 'Multiplication of '+str(num1) + ' and ' +str(num2) +' is ' +str(r)

        if operation == 'divide':
            r = num1 / num2
            math_result = 'Division of '+str(num1) + ' and ' +str(num2) +' is ' +str(r)
        
        print(math_result)
        return render_template('result.html', result = math_result)

                



    

#constructor define
if __name__ =='__main__':
    app.run()


    
