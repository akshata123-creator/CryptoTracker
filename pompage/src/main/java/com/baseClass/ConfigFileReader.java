package com.baseClass;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

public class ConfigFileReader {

	private Properties properties;
	private final String propertyFilePath = "config/Configuration.properties";

	// constructor
	public ConfigFileReader() {
		BufferedReader reader;
		try {
			reader = new BufferedReader(new FileReader(propertyFilePath));
			properties = new Properties();
			try {
				properties.load(reader);
				reader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			throw new RuntimeException("Configuration.properties not found at" + propertyFilePath);
		}
	}

	public String getString(String args) {
		String outputString = properties.getProperty(args);
		if (outputString != null)
			return outputString;
		else
			throw new RuntimeException(args + "not specified in the " + "Configuration.properties file.");
	}

}
