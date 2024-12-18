function deleteOrder(id){
    fetch(`/delete/${id}`, {
        method: "DELETE"
    }).then(response => {
        if (response.ok){  // All this function does is hits the proper end point with the proper url paramter with the dealte method triggering the function
            //and as such deleteing the relvant item 
            window.location.reload();
        }
        else{
            console.error("not ok! No delete for ", id)
        }
    }).catch(error =>{
        
        console.error("not ok! No delete for ", id, error)
    })
}