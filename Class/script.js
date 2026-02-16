class Calculator{
    // constructor
    constructor(a,b){
        this.a=a;
        this.b=b;
    }
    add(){
        console.log(this.a+this.b)
    }
    sub(){
        console.log(this.a-this.b)
    }
    multiply(){
        console.log(this.a*this.b)
    }
    divide(){
        console.log(this.a/this.b)
    }
}

var cal = new Calculator(20,30);
cal.add();