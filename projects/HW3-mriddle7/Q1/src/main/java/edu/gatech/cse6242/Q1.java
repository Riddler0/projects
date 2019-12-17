package edu.gatech.cse6242;

import org.apache.hadoop.fs.Path;
import java.util.StringTokenizer;
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Q1 {

 	public static class map extends Mapper <Object, Text, Text, Text> {

		public void map(Object key, Text value, Context context) 
			throws IOException, InterruptedException  {
			String selection = value.toString();
			StringTokenizer file = new StringTokenizer(selection, "\n");

			
			while (file.hasMoreTokens()) {
				String row = file.nextToken();
				String[] tokens = row.split("\\t");

				String id = tokens[0];
				String target = tokens[1] + "," + tokens[2];
				Text tId = new Text();
  				Text tTarg = new Text();
				tId.set(id);
				tTarg.set(target);
				context.write(tId, tTarg);
			}
		}
	}

	public static class reduce extends Reducer <Text, Text, Text, Text> {
		
		public void reduce(Text key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {

			int max = -1;
			String target = new String();
			Text rMax = new Text();

			for (Text value: values) {
				String something = value.toString();
				if (Integer.parseInt(something.split(",")[1]) > max) {
					max = Integer.parseInt(something.split(",")[1]);
  					target = something.split(",")[0];
				}
				else if(Integer.parseInt(something.split(",")[1]) == max) {
					if (Integer.parseInt(target) > Integer.parseInt(something.split(",")[0])) {
						target = something.split(",")[0];
					}
				}				
			}

			rMax.set(target + "," + max);
			context.write(key, rMax);
			
		}
	}


public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "Q1");

    	

    /* TODO: Needs to be implemented */
    job.setJarByClass(Q1.class);
    job.setMapperClass(map.class);
    job.setCombinerClass(reduce.class);
    job.setReducerClass(reduce.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
