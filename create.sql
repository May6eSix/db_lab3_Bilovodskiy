CREATE TABLE CPU(
	cpu_id SERIAL,
	cpu_dev varchar(50) NOT NULL,
	cpu_series varchar(50) NOT NULL,
	PRIMARY KEY (cpu_id)
);

CREATE TABLE GPU(
	gpu_id SERIAL,
	gpu_dev varchar(50) NOT NULL,
	gpu_series varchar(50) NOT NULL,
	PRIMARY KEY (gpu_id)
);

CREATE TABLE OS (
	os_id SERIAL,
	os_name VARCHAR(50) NOT NULL,
	PRIMARY KEY (os_id)
);


CREATE TABLE laptop (
	id SERIAL,
	name VARCHAR(100) NOT NULL,
	cpu_id INT NOT NULL,
	gpu_id INT NOT NULL,
	os_id INT NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT FK_cpu
		FOREIGN KEY (cpu_id)
			REFERENCES cpu (cpu_id) ON DELETE CASCADE,
	CONSTRAINT FK_gpu
		FOREIGN KEY (gpu_id)
	  		REFERENCES gpu (gpu_id) ON DELETE CASCADE,
	CONSTRAINT FK_os
		FOREIGN KEY (os_id)
	  		REFERENCES os (os_id) ON DELETE CASCADE
);
