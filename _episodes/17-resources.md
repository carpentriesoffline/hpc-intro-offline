---
title: "Using resources effectively"
teaching: 10
exercises: 20
questions:
- "How can I review past jobs?"
- "How can I use this knowledge to create a more accurate submission script?"
objectives:
- "Look up job statistics."
- "Make more accurate resource requests in job scripts based on data describing past performance."
keypoints:
- "Accurate job scripts help the queuing system efficiently allocate
  shared resources."
---

We've touched on all the skills you need to interact with an HPC cluster:
logging in over SSH, loading software modules, submitting parallel jobs, and
finding the output. Let's learn about estimating resource usage and why it
might matter.

## Estimating Required Resources Using the Scheduler

Although we covered requesting resources from the scheduler earlier with the
π code, how do we know what type of resources the software will need in
the first place, and its demand for each? In general, unless the software
documentation or user testimonials provide some idea, we won't know how much
memory or compute time a program will need.

> ## Read the Documentation
>
> Most HPC facilities maintain documentation as a wiki, a website, or a
> document sent along when you register for an account. Take a look at these
> resources, and search for the software you plan to use: somebody might have
> written up guidance for getting the most out of it.
{: .callout}

A convenient way of figuring out the resources required for a job to run
successfully is to submit a test job, and then ask the scheduler about its
impact using `{{ site.sched.hist }}`. You can use this knowledge to set up the
next job with a closer estimate of its load on the system. A good general rule
is to ask the scheduler for 20% to 30% more time and memory than you expect the
job to need. This ensures that minor fluctuations in run time or memory use
will not result in your job being cancelled by the scheduler. Keep in mind that
if you ask for too much, your job may not run even though enough resources are
available, because the scheduler will be waiting for other people's jobs to
finish and free up the resources needed to match what you asked for.

## Stats

Since we already submitted `pi.py` to run on the cluster, we can query the
scheduler to see how long our job took and what resources were used. We will
use `{{ site.sched.hist }}` to get statistics about `parallel-pi.sh`.

```
{{ site.remote.prompt }} {{ site.sched.hist }}
```
{: .language-bash}

{% include {{ site.snippets }}/resources/account-history.snip %}

This shows all the jobs we ran recently (note that there are multiple entries
per job). To get info about a specific job, we change command slightly.

```
{{ site.remote.prompt }} {{ site.sched.hist }} {{ site.sched.flag.histdetail }} 3939324
```
{: .language-bash}

It will show a lot of info; in fact, every single piece of info collected on
your job by the scheduler will show up here. It may be useful to specify the
infomation we want using the `-o` or `--format` option. Use the command
`sacct --helpformat` to get a list of output options.


```
{{ site.remote.prompt }} {{ site.sched.hist }} -j 3939324 -o 'JobID, AllocCPUS,State,ExitCode,Elapsed,ReqMem'
```
{: .language-bash}
```
JobID         AllocCPUS      State ExitCode    Elapsed     ReqMem 
------------ ---------- ---------- -------- ---------- ---------- 
3939324               4  COMPLETED      0:0   00:00:08     28600M 
3939324.bat+          4  COMPLETED      0:0   00:00:08            
3939324.ext+          4  COMPLETED      0:0   00:00:08            
3939324.0             4  COMPLETED      0:0   00:00:06 

```
{: .output}





> ## Discussion
>
> This view can help compare the amount of time requested and actually
> used, duration of residence in the queue before launching, and memory
> footprint on the compute node(s).
>
> How accurate were our estimates?
{: .discussion}

## Improving Resource Requests

Using the job history we can give better time estimates for our
jobs. When we overestimate the time needed to complete a job it 
makes it harder for the queuing system to accurately estimate when 
resources will become free for other jobs. 
Practically, this means that the queuing system waits
to dispatch our job until the full requested time slot opens,
instead of "sneaking it in" a much shorter window where the job could
actually finish. Specifying the expected runtime in the submission
script more accurately will help alleviate cluster congestion and may
get your job dispatched earlier.

<!-- > ## Narrow the Time Estimate
>
> Edit `parallel_pi.sh` to set a better time estimate. How close can
> you get?
>
> Hint: use `{{ site.sched.flag.time }}`.
>
> > ## Solution
> >
> > The following line tells {{ site.sched.name }} that our job should
> > finish within 2 minutes:
> >
> > ```
> > {{ site.sched.comment }} {{ site.sched.flag.time }}{% if site.sched.name == "Slurm" %} {% else %}={% endif %}00:02:00
> > ```
> > {: .language-bash}
> {: .solution}
{: .challenge} -->

{% include links.md %}
