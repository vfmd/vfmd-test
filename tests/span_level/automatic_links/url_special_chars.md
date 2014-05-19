Special chars should be percent-encoded, but only in href attr:

 - http://example.net/*#$%^&\~/blah) and <http://example.net/*#$%^&\~)/blah>
 - http://example.net/blah/*#$%^&\~) and <http://example.net/blah/*#$%^&\~)>

