var facebookProfile = {
    name: "Udacian",
    friends: 25,
    messages: ["Message 1", "Message 2", "Message 3", "Message 4"],
    postMessage: function(message){
        facebookProfile.messages.push(message);
    },
    deleteMessage: function(index){
        // In the following splice() method call,
        // - argument 1 = index from where the element has to be deleted
        // - argument 2 = count of elements to be deleted
        facebookProfile.messages.splice(index, 1);
    },
    addFriend: function(){
        facebookProfile.friends = facebookProfile.friends + 1;
        //friends += 1; // this statement is equivalent to the above
    },
    removeFriend: function(){
        if(facebookProfile.friends>0)
            facebookProfile.friends = facebookProfile.friends - 1;
    }
};

