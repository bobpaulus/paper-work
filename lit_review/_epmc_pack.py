# -*- coding: utf-8 -*-
import json
ITEMS=[
("10.1007/s12672-026-05061-6","42217128","Spatially resolved single cell analysis suggests an APOE NCF1 associated immunosuppressive niche and its prognostic signature in thyroid cancer","Discover Oncology","2026-05-30",["SC","SP","IM","AL","PR"],"High",False,"gold"),
("10.1080/15476278.2026.2670152","42153613","Thyroid cancer-derived exosomal SPP1 promotes tumor progression by driving macrophage M2 polarization through the CD44/JAK2/STAT3 signaling pathway","Organogenesis","2026-05-19",["IM","MO"],"High",False,"gold"),
("10.1530/erc-26-0088","42583701","Myeloid landscape of BRAF-mutant papillary thyroid cancer and thyroiditis","Endocrine-Related Cancer","2026-08-01",["SC","IM"],"High",False,"gold"),
("10.1002/path.70104","42557785","TIM3 as a therapeutic target in anaplastic thyroid cancer: upregulation in M2-like macrophages induced by tumor microenvironment-derived TGFbeta1","The Journal of Pathology","2026-08-05",["IM"],"High",False,"closed"),
("10.1002/cam4.72261","42702761","Single-Cell Transcriptome of Anaplastic Thyroid Cancer Reveals Immunosuppressive Tumor Microenvironment Remodeling","Cancer Medicine","2026-09-01",["SC","IM","ST"],"High",False,"gold"),
("10.1158/1078-0432.ccr-25-4488","42008746","PRECISE: A Prognostic Thyrocyte-Derived Gene Signature for Papillary Thyroid Carcinoma","Clinical Cancer Research","2026-07-01",["SC","PR","AL"],"High",False,"closed"),
("10.1038/s41416-026-03467-1","42098434","Integrated multi-omics and single-cell analyses identify metabolic heterogeneity and therapeutic vulnerabilities in medullary thyroid cancer","British Journal of Cancer","2026-05-07",["ME","SC","ST"],"High",False,"closed"),
("10.1186/s13046-026-03675-w","41761234","Mechanism of cancer-associated fibroblast-driven thyroid cancer dedifferentiation via the ZFP57-PKM2 axis-mediated lactate secretion and therapeutic intervention with resveratrol","Journal of Experimental & Clinical Cancer Research","2026-02-27",["SP","ME","ST","IM"],"High",False,"gold"),
("10.1016/j.xcrm.2026.102661","41794039","Proteogenomic characterization delineates clinically relevant subtypes of advanced differentiated thyroid cancer","Cell Reports Medicine","2026-03-06",["MO","SP","AL","IM"],"High",False,"gold"),
("10.1210/endocr/bqag012","41631714","Single-cell analysis identifies ATC-like cells driving progression in relapsed follicular thyroid carcinoma","Endocrinology","2026-02-01",["SC","ST"],"High",False,"closed"),
("10.3390/ijms27167387","42653390","CREM Marks TCR-Driven T-Cell Activation and Associates with Favorable Prognosis in Papillary Thyroid Carcinoma","International Journal of Molecular Sciences","2026-08-18",["SC","IM","PR"],"Medium",False,"gold"),
("10.1093/gpbjnl/qzag060","42412534","Single-cell RNA Sequencing Reveals A Tumor-Promoting Role of EGR1+CD4+ T Cells in Papillary Thyroid Cancer","Genomics, Proteomics & Bioinformatics","2026-07-07",["SC","IM"],"Medium",False,"closed"),
("10.1038/s41598-026-41927-z","41748865","Visualizing malignant progression: in situ CD109-based spatial immunofluorescence assay delineates papillary to anaplastic thyroid carcinoma transformation within the TME","Scientific Reports","2026-02-26",["SP","IM","ST"],"Medium",False,"gold"),
("10.1002/cam4.71766","41957879","Integrative Single-Cell and Machine Learning Analysis Identifies an EMT-Associated Prognostic Signature for Papillary Thyroid Cancer","Cancer Medicine","2026-04-01",["SC","AL","ST"],"Medium",False,"gold"),
("10.2147/itt.s565624","41859299","Macrophage-Derived Transcriptional Signatures Predict Prognosis and Drug Sensitivity in Thyroid Cancer: Integrative Analysis and Experimental Validation of SMYD3","ImmunoTargets and Therapy","2026-01-09",["IM","AL","PR"],"Medium",False,"gold"),
("10.1007/s10238-026-02101-x","41739250","CD44 is associated with papillary thyroid carcinoma metastasis via potential modulation of the immunosuppressive tumor microenvironment","Clinical and Experimental Medicine","2026-02-25",["IM","PR"],"Medium",False,"gold"),
("10.1016/j.jpha.2025.101354","41626563","CXCL8/SDC1 axis mediates tumor stem cell interactions to drive remote transfer in thyroid cancer","Journal of Pharmaceutical Analysis","2025-06-02",["SC","SP","ST"],"Medium",False,"gold"),
("10.1038/s41540-026-00663-w","41826383","Integrated multi-omics and single-cell analysis reveals CDKN2A-mediated cuproptosis mechanisms driving thyroid carcinoma progression","npj Systems Biology and Applications","2026-03-13",["ME","MO","IM"],"Medium",False,"gold"),
("10.21203/rs.3.rs-9248842/v1",None,"C/EBPbeta Drives Anaplastic Thyroid Cancer Dedifferentiation and Radioiodine Resistance via IL-6/JAK/STAT and EMT Activation","Research Square [preprint]","2026-05-18",["SC","SP","ST","ME"],"Medium",True,"green"),
("10.1007/s12672-026-04601-4","41663780","JAG1 expression in papillary thyroid cancer stem-like cells predicts poor prognosis and implicates angiogenesis","Discover Oncology","2026-02-09",["SC","ST"],"Medium",False,"gold"),
("10.1007/s12020-026-04552-4","41697550","Spatial proteomics and machine learning reveal diagnostic protein signatures for indeterminate thyroid nodules","Endocrine","2026-02-16",["SP","AL"],"Medium",False,"closed"),
("10.1186/s13044-026-00306-6","42363265","Single-cell RNA sequencing in thyroid cancer: a methodological review and thyroid specific dissociation protocol","Thyroid Research","2026-06-26",["SC"],"Medium",False,"closed"),
("10.1007/s00405-026-10456-w","42472943","Comprehensive evaluation of angiogenesis-associated genes in papillary thyroid cancer using bulk RNA and single-cell sequencing data","European Archives of Oto-Rhino-Laryngology","2026-07-19",["MO","SC"],"Low",False,"closed"),
]
LAB={"MO":"分子机制","IM":"免疫微环境","SC":"单细胞","SP":"空间组学","AL":"算法方法","PR":"预后转移","ST":"转移干性","ME":"代谢重编程"}
recs=[]
for doi,pmid,title,venue,date,dims,rel,ispre,oa in ITEMS:
    recs.append(dict(pmid=pmid,doi=doi,openalex_id=None,title=title,abstract=None,
        publication_date=date,type="preprint" if ispre else "article",is_preprint=ispre,
        venue=venue,oa_status=oa,oa_url=None,cited_by_count=None,in_scope_thyroid=True,
        exclude_reason=None,versions=[],queries=["epmc-supplement"],dimensions=dims,
        dimension_labels=[LAB[d] for d in dims],relevance=rel,source="EuropePMC"))
json.dump(recs,open('_epmc_pack_run24.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("epmc supplement records:",len(recs))
