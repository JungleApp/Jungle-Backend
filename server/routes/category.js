/**
 * Created by patilramya on 4/14/17.
 */
var express = require('express');
var mongoose = require('mongoose');
var router = express.Router();
var databaseCall = require('../utility/databaseCalls');
var categorySchema = mongoose.model('category');

// routes
router.post('/request', requestCategory);
router.get('/get', getCategory);
router.get('/get/:id', getCategoryById);
router.put('/approve/:name', approveCategory);
router.put('/update/:id', updateCategory);
router.delete('/delete/:name', deleteCategory);

module.exports = router;

/**
 *  Request a new category for NGO
 *  Request data:
 *  {
 *      "name" : "Environment"
 *  }
 */
function requestCategory(req,res){
    var newCategory = new categorySchema();
    newCategory.name = req.body.name.toLowerCase();
    databaseCall.saveQuery(newCategory).then(function (result) {
        res.json(result);
    }).catch(function (err) {
        res.json(err);
    });
}

/**
 * Get all categories
 */
function getCategory(req,res){
    var object = {};
    object['valid'] = true;
    databaseCall.findQuery(categorySchema,object).then(function (response){
        res.json(response.data);
    });
}

/**
 * Get category data by id
 */
function getCategoryById(req,res){
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(categorySchema,object).then(function (response){
        res.json(response);
    });
}

/**
 * Approve category
 */
function approveCategory(req,res){
    var object = {};
    object['name'] = req.params.name.toLowerCase();
    databaseCall.findOneQuery(categorySchema,object).then(function (response){
        if (response.success) {
            var updateData = {};
            updateData.valid = true;
            databaseCall.updateQuery(categorySchema, object, updateData, false).then(function (response) {
                res.json(response);
            });
        } else {
            res.json(response);
        }
    });
}

/**
 * Update category data by id
 */
function updateCategory(req,res){
    var object = {};
    object['_id'] = mongoose.Types.ObjectId(req.params.id);
    databaseCall.findOneQuery(categorySchema,object).then(function (response){
        if (response.success) {
            var updateData = {};
            updateData.name = req.body.name.toLowerCase();
            updateData.valid = false;
            databaseCall.updateQuery(categorySchema, object, updateData, false).then(function (response) {
                res.json(response);
            });
        } else {
            res.json(response);
        }
    });
}

/**
 * Delete category data by name
 */
function deleteCategory(req,res){
    var object = {};
    object['name'] = req.params.name.toLowerCase();
    databaseCall.deleteQuery(categorySchema, object).then(function (response) {
        res.json(response);
    });
}