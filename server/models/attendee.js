/**
 * Attendee Schema Model
 * Created 4/15/17 @jessebartola
 */

var mongoose = require('mongoose');

/** 
 * Define Attendee Schema
 *
 * Represents the many-to-many relationship between User and Event documents
 */

var attendeeSchema = new mongoose.Schema({
    user: {
        type: Schema.Types.ObjectID,
        required: true
    },
    event: {
        type: Schema.Types.ObjectID,
        required: true
    },
    confirmed: {
        type: Boolean,
        default: false
    }
});

mongoose.model('attendee', attendeeSchema, 'attendee');