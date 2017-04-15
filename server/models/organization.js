/**
 * Created by patilramya on 4/8/17.
 */
var mongoose = require('mongoose');
var bcrypt = require('bcrypt-nodejs');

//Definition of the NGO schema
var ngoSchema = new mongoose.Schema({
    name : String,
    email: {
        type: String,
        unique: true
    },
    username: {
        type: String,
        unique: true
    },
    password : String,
    description : String,
    causes : [],
    location : {
        country: String,
        city: String
    }
});

// generating a hash
ngoSchema.methods.generateHash = function(password) {
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

// checking if password is valid
ngoSchema.methods.validPassword = function(password) {
    return bcrypt.compareSync(password, this.password);
};

mongoose.model('organization', ngoSchema, 'organization');