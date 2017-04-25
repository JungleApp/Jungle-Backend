/**
 * Passport.js Authentication
 * Created 4/17/17 @jessebartola
 */

var passport = require('passport');
BasicStrategy = require('passport-http').BasicStrategy;
var databaseCall = require('databaseCalls');
var ngoSchema = mongoose.model('../routes/organization');
var messages = require('messages');

// Define new username/password login strategy
passport.use(new BasicStrategy(
    function(username, password, done) {
        databaseCall.findOneQuery(ngoSchema, {'username': username}).then(function (response){
            var currentUser = response.data;

            // Db is not available
            if (response.isError) {

                return done(null, false, { message: 'Database not available'});

            } else if (response.errorMessage = messages.NOT_FOUND) {

                return done(null, false, { message: 'Invalid username.'});

            } else if (!currentUser.validPassword(password)) {

                return done(null, false, { message: 'Invalid password.'});

            } else {
                // If we have a valid username and correct password, confirm authentication
                return done(null, currentUser);
            }
            
        });
    }
));

var authentication = passport.authenticate('basic', { session: false });
module.exports.authentication = authentication;
