-- cpu
INSERT INTO cpu (cpu_dev, cpu_series)
  	VALUES ('Intel', 'i5-7400');
INSERT INTO cpu (cpu_dev, cpu_series)
  	VALUES ('Intel', 'i3-6100');
INSERT INTO cpu (cpu_dev, cpu_series)
  	VALUES ('AMD', 'FX 6700');
INSERT INTO cpu (cpu_dev, cpu_series)
  	VALUES ('AMD', 'Ryzen 5 2200');
INSERT INTO cpu (cpu_dev, cpu_series)
  	VALUES ('Qualcomm', 'Wh355');

-- gpu
INSERT INTO gpu (gpu_dev, gpu_series)
  	VALUES ('NVIDIA', 'gt 730');
INSERT INTO gpu (gpu_dev, gpu_series)
  	VALUES ('NVIDIA', 'gtx 1060');
INSERT INTO gpu (gpu_dev, gpu_series)
  	VALUES ('AMD', 'rx 560x');
INSERT INTO gpu (gpu_dev, gpu_series)
  	VALUES ('AMD', 'vega 8');
INSERT INTO gpu (gpu_dev, gpu_series)
  	VALUES ('Intel', 'IRIS PRO 6300');

--os
insert into os(os_name)
	values('Windows 11');
insert into os(os_name)
	values('Windows 10');
insert into os(os_name)
	values('MacOS');
insert into os(os_name)
	values('Linux Ubuntu');
insert into os(os_name)
	values('without os');



-- laptop
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('Macbook Air 2017', 
			1, 5, 3);
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('Macbook pro 15 inch 2018', 
			5, 2, 3);
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('Acer Nitro 5 F-3456', 
			4, 3, 5);
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('Acer Nitro 5 F-3457', 
			4, 3, 2);
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('Asus Notepad', 
			2, 1, 1);
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('HP Pavilion', 
			3, 4, 4);
INSERT INTO laptop (name , cpu_id, gpu_id, os_id)
	VALUES ('Vivo laptop', 
			3, 1, 5);
