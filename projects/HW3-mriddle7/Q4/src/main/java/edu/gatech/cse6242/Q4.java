package edu.gatech.cse6242;

import org.apache.hadoop.fs.Path;
import java.util.StringTokenizer;
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

public class Q4 {

	public static class map1 
	extends Mapper <Object, Text, IntWritable, IntWritable>{
		public void map(Object key, Text value, Context context )
			throws IOException, InterruptedException {

				String selection = value.toString();
				StringTokenizer file = new StringTokenizer(selection, "\n");

				while (file.hasMoreTokens()) {

					String row = file.nextToken();
					String[] tokens = row.split("\\t");

					String source = tokens[0];
					String target = tokens[1];

					int int_tSrc = Integer.parseInt(source);
					int int_tTarg = Integer.parseInt(target);

					IntWritable tSrc = new IntWritable();
  					IntWritable tTarg = new IntWritable();

					tSrc.set(int_tSrc);
					tTarg.set(int_tTarg);

					IntWritable node_in = new IntWritable(1);
					IntWritable node_out = new IntWritable(-1);

					context.write(tSrc, node_in);
					context.write(tTarg, node_out);
					}
				}
			}

	public static class reduce1
	extends Reducer <IntWritable, IntWritable, IntWritable, IntWritable>{
		public void reduce(IntWritable key, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException{

			int node_counting = 0;
			for (IntWritable value: values) {
				node_counting += value.get();
			}

			IntWritable node_diff = new IntWritable();
			node_diff.set(node_counting);
			context.write(key, node_diff);
		}
	}

	public static class map2
	extends Mapper <Object, Text, IntWritable, IntWritable>{
		public void map(Object key, Text value, Context context)
			throws IOException, InterruptedException{
			IntWritable node_degree_present = new IntWritable(1);

			String selection2 = value.toString();
			StringTokenizer file2 = new StringTokenizer(selection2, "\n");

			while (file2.hasMoreTokens()) {

			String row2 = file2.nextToken();
			String[] tokens2 = row2.split("\\t");

			int diff_presence = Integer.parseInt(tokens2[1]);

			IntWritable diff_presence_writable = new IntWritable();
			diff_presence_writable.set(diff_presence);
			context.write(diff_presence_writable, node_degree_present);

	
			}
		}
	}

	public static class reduce2
	extends Reducer <IntWritable, IntWritable, IntWritable, IntWritable>{
		public void reduce(IntWritable key, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException{

			int sum_node_degree_present = 0;

			for (IntWritable value: values) {
				sum_node_degree_present += value.get();
			}
			
			IntWritable sum_node_degree_present_writable = new IntWritable();
			sum_node_degree_present_writable.set(sum_node_degree_present);
			context.write(key, sum_node_degree_present_writable);
		}
	}


public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "Q4");
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1] + "out1"));

    /* TODO: Needs to be implemented */
    job.setJarByClass(Q4.class);
    job.setMapperClass(map1.class);
    job.setCombinerClass(reduce1.class);
    job.setReducerClass(reduce1.class);
    job.setOutputKeyClass(IntWritable.class);
    job.setOutputValueClass(IntWritable.class);

	job.waitForCompletion(true);
	
	Configuration conf2 = new Configuration();
    Job job2 = Job.getInstance(conf2, "Q4");
    job2.setJarByClass(Q4.class);
    job2.setMapperClass(map2.class);
    job2.setCombinerClass(reduce2.class);
    job2.setReducerClass(reduce2.class);
    job2.setOutputKeyClass(IntWritable.class);
    job2.setOutputValueClass(IntWritable.class);

    FileInputFormat.addInputPath(job2, new Path(args[1] + "out1"));
    FileOutputFormat.setOutputPath(job2, new Path(args[1]));
    System.exit(job2.waitForCompletion(true) ? 0 : 1);
}
}

