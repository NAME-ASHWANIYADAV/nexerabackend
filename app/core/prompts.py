# backend/app/core/prompts.py

def get_profile_extraction_prompt(resume_text: str):
    # ... (existing prompt from Phase 1) ...
    system_prompt = """
You are a highly accurate resume parsing AI. Your task is to extract structured information from the provided resume text and return it as a valid JSON object. Do not add any extra commentary. The JSON object must strictly conform to the following schema:
{
  "summary": "string",
  "skills": ["string"],
  "experiences": [
    {
      "role": "string",
      "company": "string",
      "duration": "string (e.g., 'Jan 2022 - Present' or '3 years')",
      "bullet_points": ["string"]
    }
  ],
  "educations": [
    {
      "degree": "string",
      "institution": "string",
      "graduation_year": "string (optional)"
    }
  ]
}
"""
    user_prompt = f"""
Here is the resume text. Please extract the information and provide it as a single JSON object.

<resume_text>
{resume_text}
</resume_text>
"""
    return system_prompt, user_prompt


def get_ats_optimization_prompt(original_resume_text: str, job_description: str, custom_instructions: str = None):
    # This is the final, copy-paste ready prompt, now with refinement capabilities
    system_prompt = """
You are an expert resume writer specializing in optimizing resumes for Applicant Tracking Systems (ATS), particularly for the Indian job market (portals like Naukri, LinkedIn India, etc.). Your goal is to rewrite a resume to maximize its chances of passing through an ATS for a specific job description, while adhering to strict constraints.
"""

    # Add custom instructions if provided for the refinement loop
    instructions_block = ""
    if custom_instructions:
        instructions_block = f"""
**USER REFINEMENT INSTRUCTIONS:**
- {custom_instructions}

Please incorporate these instructions while performing the rewrite.
"""

    user_prompt = f"""
I will provide you with an original resume and a job description. Your task is to rewrite the content of the resume to better match the job description.

{instructions_block}

**VERY IMPORTANT RULES:**

1.  **DO NOT CHANGE THE STRUCTURE OR LAYOUT.** The output must have the exact same sections, headings, and order as the original resume. Do not add, remove, or reorder any sections.
2.  **REWRITE WORDING ONLY.** Focus on improving bullet points, using stronger action verbs, and quantifying achievements where possible.
3.  **INJECT KEYWORDS.** Seamlessly integrate relevant keywords and skills from the job description into the resume content. Make it sound natural.
4.  **PLAIN TEXT OUTPUT ONLY.** Do not use any Markdown, HTML, or other formatting. The output should be simple, clean text that can be copied and pasted anywhere.
5.  **PRESERVE ALL PERSONAL INFORMATION.** Do not change the name, contact details, or any other personal identifiers.
6.  **MAINTAIN HONESTY.** Do not invent skills or experiences. Enhance what is already there.

Here is the original resume text:
<original_resume>
{original_resume_text}
</original_resume>

Here is the target job description:
<job_description>
{job_description}
</job_description>

Now, please provide the rewritten, ATS-optimized resume text inside `<optimized_resume></optimized_resume>` tags.
"""
    return system_prompt, user_prompt

def get_match_explanation_prompt(profile_summary: str, profile_skills: list, job_title: str, job_description: str) -> (str, str):
    """
    New prompt for generating the "Why you're a good match" explanation.
    """
    system_prompt = """
You are a helpful career assistant. Your task is to analyze a user's profile against a job description and provide a brief, honest, and encouraging explanation of why the job is a good match.
The output must be in bullet points. Do not be overly enthusiastic or use marketing language. Be specific.
"""
    
    user_prompt = f"""
A user's profile has the following summary and skills:
<profile_summary>
{profile_summary}
</profile_summary>
<profile_skills>
{', '.join(profile_skills)}
</profile_skills>

The user is being matched with the following job:
<job_title>
{job_title}
</job_title>
<job_description>
{job_description}
</job_description>

Please generate 3-5 bullet points explaining why this job is a good potential match for the user. Focus on skill overlap, experience relevance, and role alignment.
"""
    return system_prompt, user_prompt