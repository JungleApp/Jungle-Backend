/**
 * Event API Handler
 * Created 4/15/17 @jessebartola
 */

var express = require('express');
var mongoose = require('mongoose');
var router = express.Router();
var databaseCall = require('../utility/databaseCalls');
var eventSchema = mongoose.model('event');

// API Routes
router.post('/create', makeEvent);
router.get('/get/:id', getEventById);
router.get('/get', getAllEvents);
router.put('/update/:id', updateById);
router.delete('/delete/:id', deleteEvent);

module.exports = router;

/*
 * Create Event POST route
 */
function makeEvent(req, res){
    var newEvent = new eventSchema();
    newEvent.title = req.body.title;
    newEvent.host = mongoose.Types.ObjectId(req.body.host);
    newEvent.description = req.body.description;
    newEvent.time.start = req.body.time.start;
    databaseCall.saveQuery(newEvent).then(function (result) {
        res.json(result);
    }).catch(function (err) {
        res.json(err);
    });
}

/**
 * Get Event by ObjectID
 */
function getEventById(req, res) {
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(eventSchema,object).then(function (response){
        res.json(response);
    });
}

/**
 * Get all Events
 */
function getAllEvents(req,res){
    var object = {};
    databaseCall.findQuery(eventSchema, object).then(function (response){
        res.json(response.data);
    });
}

/**
 * Update Event by ObjectID
 */
function updateById(req, res){
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(eventSchema,object).then(function (response){
        if (response.success) {
            var updateEvent = req.body;
            databaseCall.updateQuery(eventSchema, object, updateEvent, false).then(function (response) {
                res.json(response);
            });
        } else {
            res.json(response);
        }
    });
}

/**
 * Delete event by ObjectID
 */
function deleteEvent(req, res) {
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.deleteQuery(eventSchema, object).then(function (response) {
        res.json(response);
    });
}
