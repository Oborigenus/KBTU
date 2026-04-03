CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT[], p_phone TEXT[])
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        
        -- phone validation (only digits, length 10-15)
        IF phones[i] ~ '^[0-9]{10,15}$' THEN
            
            IF EXISTS (SELECT 1 FROM contacts WHERE name = names[i]) THEN
                UPDATE contacts SET phone = phones[i]
                WHERE name = names[i];
            ELSE
                INSERT INTO contacts(name, phone)
                VALUES (names[i], phones[i]);
            END IF;

        ELSE
            RAISE NOTICE 'Invalid phone: % for %', phones[i], names[i];
        END IF;

    END LOOP;
END;
$$;