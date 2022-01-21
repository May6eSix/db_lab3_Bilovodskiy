DO $$
DECLARE
    os_id  os.os_id%TYPE;
    os_name   os.os_name%TYPE;

BEGIN
    os_id := 10;
    os_name := 'OS_Name';
    FOR counter IN 1..10
        LOOP
            INSERT INTO os(os_id, os_name)
            VALUES (os_id + counter, os_name || counter);
        END LOOP;
END;
$$
 --select * from os
