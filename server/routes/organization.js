/**
 * Created by patilramya on 4/14/17.
 */
var express = require('express');
var mongoose = require('mongoose');
var router = express.Router();
var databaseCall = require('../utility/databaseCalls');
var ngoSchema = mongoose.model('organization');

// routes
router.post('/signup', registerNGO);
router.get('/getOrg', getOrgData);
router.get('/get/:id', getOrgById);
router.get('/get', getAllOrg);
router.put('/update/:id', updateById);
router.delete('/delete/:id', deleteOrg);

module.exports = router;

/**
 *  Save data to organisation schema
 *  Request data:
 *  {
 *      "username" : "youth4seva",
 *      "password" : "youth4seva",
 *      "email" : "contact@youthforseva.org",
 *      "name" : "Youth For Seva"
 *  }
 */
function registerNGO(req, res){
    var newOrg = new ngoSchema();
    newOrg.username = req.body.username;
    newOrg.password = newOrg.generateHash(req.body.password);
    newOrg.email = req.body.email;
    newOrg.name = req.body.name;
    databaseCall.saveQuery(newOrg).then(function (result) {
        res.json(result);
    }).catch(function (err) {
        res.json(err);
    });
}

/**
 * Get organisation details by email
 */
function getOrgData(req, res) {
    var object = {};
    object['email'] = req.query.email;
    databaseCall.findOneQuery(ngoSchema,object).then(function (response){
        res.json(response);
    });
}

/**
 * Get organisation details by id
 */
function getOrgById(req, res) {
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(ngoSchema,object).then(function (response){
        res.json(response);
    });
}

/**
 * Get all organisations details
 */
function getAllOrg(req,res){
    var object = {};
    databaseCall.findQuery(ngoSchema,object).then(function (response){
        res.json(response.data);
    });
}

/**
 * Update organisation data by id
 */
function updateById(req, res){
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(ngoSchema,object).then(function (response){
        if (response.success) {
            var updateOrg = req.body;
            databaseCall.updateQuery(ngoSchema, object, updateOrg, false).then(function (response) {
                res.json(response);
            });
        } else {
            res.json(response);
        }
    });
}

/**
 * Delete organisation data by id
 */
function deleteOrg(req, res) {
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.deleteQuery(ngoSchema, object).then(function (response) {
        res.json(response);
    });
}

