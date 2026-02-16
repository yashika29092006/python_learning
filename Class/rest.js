// rest 

const details ={
    name:"yashika",
    id: 1,
    email:"yashika@gmail.com",
    role:"Admin"
};
// destructing
const {name,id,...rest}=details;
console.log(name)
console.log(rest)

left = [10,20,30]
right = [40,50,60]


// rest in function , use this method when you don't know the how much params 
function total(...rest){
    console.log(rest)
}
total(1,2,3)
// this method eliminate first 2 params
function total(a,b,...rest){
    console.log(rest)
}
total(1,2,3)

let products={
    names :"apple macbook pro",
    price : 2500,
    currency:"INR"
};
let ratings ={
    rating:5,
    feedback:['good','ok','bad']
}

let {names,price}=products;
result = {names:names,price:price,...ratings};
console.log(result)
