/**
 * Created by patilramya on 4/8/17.
 */
var mongoose = require('mongoose');

//Definition of the category (causes NGO support) schema
var categorySchema = new mongoose.Schema({
    name : {
        type: String,
        unique: true
    },
    valid : {
        type: Boolean,
        default: false
    }
});

mongoose.model('category', categorySchema, 'category');