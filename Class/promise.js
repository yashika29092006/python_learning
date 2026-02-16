// const processA = new Promise((resolve,reject)=>{
//     if (2>3) resolve('2 is lesser than 3');
//     else reject('some error happened')
// });

// processA
//     .then(function (result) {
//         console.log(result)
//     })
//     .catch(function(err) {
//         console.log(err);
//     })
async function stations(){
    try{
        let user = await fetch(
            'https://restcountries.com/v3.1/all'
        )
        let data = await user.json();
        console.log(data);
    }
    catch(error){
        console.log(error)
    }
}
stations()