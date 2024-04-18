# Data Visualization Guide Dataset

This dataset provides guidance for selecting effective data visualization techniques. It's designed to be used within a software tool aiding in automated chart and graph generation based on data characteristics and user requests.

## Database Structure

The dataset is normalized into several tables within an SQLite database. 

* **visual_aids.db**

Tables:

* **visual_aids:** Contains core information about each visualization type.
    * Columns: visual_aid_id (primary key), name, visual_aid_category, definition,  data_types_good_for, data_types_not_good_for, audience, audience_skill_level, audience_focus, cognitive_load
* **design_principles:** A comprehensive list of design principles for effective visualizations.
    * Columns: design_principle_id (primary key), design_principle, description
* **design_principles_junction:** Links visual aids to relevant design principles (many-to-many relationship).
    * Columns: data_type_id, design_principle_id (with appropriate foreign key constraints)

* **Additional Tables** 
   You may consider creating similar tables for 'contexts' and 'audience' if these columns become too complex to manage within the visual_aids table.

## Usage Notes

* Table relationships and foreign keys ensure data integrity.
* The 'Audience Skill Level' and 'Cognitive Load' columns are somewhat subjective and depend upon the quality of the specific visualization's design.
* Your visualization tool will need logic to interpret this data and make informed decisions about the best visual representations.

## Contribution

This dataset is an ongoing project. Feel free to submit pull requests (or suggest changes in this README) to add new visual aids, enhance descriptions, or expand the design principles.
