/**
 * Event Schema Model
 * Created 4/15/17 @jessebartola
 */

var mongoose = require('mongoose');

// Define Event Schema
var eventSchema = new mongoose.Schema({
    title: { 
    	type: String,
    	required: true
    },
    // Foreign key referencing NGO schema
    host: {
    	type: Schema.Types.ObjectId,
    	required: true
    },
    description: String,
    time: {
    	start: {
    		type: Date,
    		required: true
    	},
    	end: Date
    },
    location: {
    	country: String,
    	city: String
    },
    banner_picture: String
});

mongoose.model('event', eventSchema, 'event');