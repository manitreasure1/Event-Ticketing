

-- SELECT userdb.username, organization.*
-- FROM organization
-- JOIN userdb ON organization.created_by = userdb.id;

SELECT userdb.username, organization.*, userorganization.*
FROM organization
JOIN userorganization ON organization.id = userorganization.organization_id
JOIN userdb ON userorganization.user_id = userdb.id;