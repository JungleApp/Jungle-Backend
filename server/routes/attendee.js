/**
 * Attendee API Handler
 * Created 4/15/17 @jessebartola
 */

var express = require('express');
var mongoose = require('mongoose');
var router = express.Router();
var databaseCall = require('../utility/databaseCalls');
var attendeeSchema = mongoose.model('attendee');

// API Routes
router.post('/create', makeAttendee);
router.get('/get/:id', getAttendeeById);
router.get('/get/user/:user_id', getAttendeesByUser);
router.get('/get/party/:event_id', getAttendeesByEvent);
router.get('/get/:user_id/:event_id', getAttendeeByIds);
router.put('/update/:id', updateAttendeeById);
router.put('/update/:user_id/:event_id', updateAttendeeByIds);
router.delete('/delete/:id', deleteAttendee);

module.exports = router;

/*
 * Create Attendee POST route
 */
function makeAttendee(req, res){
    var newAttendee = new attendeeSchema();
    newAttendee.user = mongoose.Types.ObjectId(req.body.user);
    newAttendee.event = mongoose.Types.ObjectId(req.body.event);
    databaseCall.saveQuery(newAttendee).then(function (result) {
        res.json(result);
    }).catch(function (err) {
        res.json(err);
    });
}

/**
 * Get Attendee by ID
 */
function getAttendeeById(req, res) {
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(attendeeSchema, object).then(function (response) {
        res.json(response);
    });
}

/**
 * Get Attendees by UserID
 */
function getAttendeesByUser(req, res) {
    var object = {};
    object['user'] = mongoose.Types.ObjectId(req.params.user_id);
    databaseCall.findQuery(attendeeSchema, object).then(function (response) {
        res.json(response);
    });
}

/**
 * Get Attendees by EventID
 */
function getAttendeesByEvent(req, res) {
    var object = {};
    object['event'] = mongoose.Types.ObjectId(req.params.event_id);
    databaseCall.findQuery(attendeeSchema, object).then(function (response) {
        res.json(response);
    });
}

/**
 * Get Attendee by UserID & EventID
 */
function getAttendeeByIds(req, res) {
    var object = {};
    object['user_id'] = mongoose.Types.ObjectId(req.params.user_id);
    object['event_id'] = mongoose.Types.ObjectId(req.params.event_id);
    databaseCall.findOneQuery(attendeeSchema, object).then(function (response) {
        res.json(response);
    });
}

/**
 * Update Attendee by ObjectID
 */
function updateAttendeeById(req, res){
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(eventSchema, object).then(function (response){
        if (response.success) {
            var updateAttendee = req.body;
            databaseCall.updateQuery(attendeeSchema, object, updateAttendee, false).then(function (response) {
                res.json(response);
            });
        } else {
            res.json(response);
        }
    });
}

/**
 * Update Attendee by UserID & EventID
 */
function updateAttendeeByIds(req, res){
    var object = {};
    object['user_id'] = mongoose.Types.ObjectId(req.params.user_id);
    object['event_id'] = mongoose.Types.ObjectId(req.params.event_id);
    databaseCall.findOneQuery(attendeeSchema,object).then(function (response){
        if (response.success) {
            // Retrieve new attendee attributes from body of the request
            var updateAttendee = req.body;
            databaseCall.updateQuery(attendeeSchema, object, updateAttendee, false).then(function (response) {
                res.json(response);
            });
        } else {
            res.json(response);
        }
    });
}

/**
 * Delete Attendee by ObjectID
 */
function deleteAttendee(req, res) {
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.deleteQuery(attendeeSchema, object).then(function (response) {
        res.json(response);
    });
}
